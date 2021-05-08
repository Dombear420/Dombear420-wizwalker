from typing import Union

import wizwalker


# TODO: add way to cast spells like pixie
class CombatCard:
    """
    Represents a spell card
    """

    def __init__(
        self, combat_handler, spell_window: "wizwalker.memory.window.DynamicWindow",
    ):
        self.combat_handler = combat_handler

        self._spell_window = spell_window

    async def cast(self, target: Union["CombatCard", "wizwalker.combat.CombatMember"]):
        # handle the combat card and combat member types
        # check they're able to enchant/cast

        # TODO enchants
        if isinstance(target, CombatCard):
            pass

        else:
            # TODO: checks
            await self.combat_handler.client.mouse_handler.click_window(
                self._spell_window
            )
            await self.combat_handler.client.mouse_handler.click_window(
                target._combatant_control
            )

    async def get_graphical_spell(
        self,
    ) -> "wizwalker.memory.spell.DynamicGraphicalSpell":
        """
        The GraphicalSpell with information about this card
        """
        return await self._spell_window.maybe_graphical_spell()

    async def name(self) -> str:
        """
        The name of this card (display)
        """
        graphical_spell = await self.get_graphical_spell()
        spell_template = await graphical_spell.spell_template()
        return await spell_template.display_name()

    async def template_id(self) -> int:
        """
        This card's template id
        """
        graphical_spell = await self.get_graphical_spell()
        return await graphical_spell.template_id()

    async def spell_id(self) -> int:
        """
        This card's spell id
        """
        graphical_spell = await self.get_graphical_spell()
        return await graphical_spell.spell_id()

    # TODO: test with accuracy enchants
    async def accuracy(self) -> int:
        """
        Current accuracy of this card
        """
        graphical_spell = await self.get_graphical_spell()
        return await graphical_spell.accuracy()

    async def is_treasure_card(self) -> bool:
        """
        If this card is a treasure card
        """
        graphical_spell = await self.get_graphical_spell()
        return await graphical_spell.treasure_card()

    async def is_item_card(self) -> bool:
        """
        If this card is an item card
        """
        graphical_spell = await self.get_graphical_spell()
        return await graphical_spell.item_card()

    async def is_side_board(self) -> bool:
        """
        If this card is from the side deck
        """
        graphical_spell = await self.get_graphical_spell()
        return await graphical_spell.side_board()

    async def is_cloaked(self) -> bool:
        """
        If this card is cloaked
        """
        graphical_spell = await self.get_graphical_spell()
        return await graphical_spell.cloaked()

    async def is_enchanted_from_item_card(self) -> bool:
        """
        If this card was enchanted from an item card
        """
        graphical_spell = await self.get_graphical_spell()
        return await graphical_spell.enchantment_spell_is_item_card()

    async def is_pve_only(self) -> bool:
        """
        If this card can only be used in pve
        """
        graphical_spell = await self.get_graphical_spell()
        return await graphical_spell.pve()
